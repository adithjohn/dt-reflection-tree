# -*- coding: utf-8 -*-


import json
import re

# ---------- LOAD FILE ----------
with open("reflection-tree.json") as f:
    node_list = json.load(f)

nodes = {n["id"]: n for n in node_list}

# ---------- STATE ----------
state = {
    "answers": {},
    "axis1": {"internal": 0, "external": 0},
    "axis2": {"contribution": 0, "entitlement": 0, "neutral": 0},
    "axis3": {"self": 0, "team": 0, "individual": 0, "system": 0}
}

# ---------- HELPERS ----------

def get_children(node_id):
    return sorted(
        [n for n in nodes.values() if n.get("parentId") == node_id],
        key=lambda x: x["id"]
    )

def next_node(node):
    if "target" in node:
        return node["target"]
    children = get_children(node["id"])
    return children[0]["id"] if children else None

def apply_signal(signal):
    axis, value = signal.split(":")
    if axis in state and value in state[axis]:
        state[axis][value] += 1

def fix_condition(condition):
    """Convert axis1.internal → axis1['internal'] automatically"""
    condition = re.sub(r"(axis[123])\.(\w+)", r"\1['\2']", condition)
    return condition

def evaluate_condition(condition):
    try:
        original = condition

        # Replace answer references
        for key, val in state["answers"].items():
            condition = condition.replace(f"{key}.answer", f"'{val}'")

        # Fix axis syntax
        condition = fix_condition(condition)

        result = eval(condition, {}, {
            "axis1": state["axis1"],
            "axis2": state["axis2"],
            "axis3": state["axis3"]
        })

        return result

    except Exception as e:
        print(f"\n⚠️ Condition error: {original}")
        return False

def run_decision(node):
    for rule in node["rules"]:
        if evaluate_condition(rule["if"]):
            return rule["goTo"]
    return None

def interpolate(text):
    for key, val in state["answers"].items():
        text = text.replace(f"{{{key}.answer}}", val)
    return text

# ---------- ENGINE ----------

current = "START"
current = next_node(nodes[current])

visited = set()

while current:

    if current in visited:
        print("\n⚠️ Loop detected. Exiting.")
        break
    visited.add(current)

    node = nodes[current]

    # ---------- DISPLAY ----------
    if "text" in node:
        print("\n" + interpolate(node["text"]))

    # ---------- QUESTION ----------
    if node["type"] == "question":

        for i, opt in enumerate(node["options"]):
            print(f"{i+1}. {opt}")

        while True:
            user_input = input("> ").strip()

            # Number input
            if user_input.isdigit():
                choice = int(user_input) - 1
                if 0 <= choice < len(node["options"]):
                    break

            # Text input
            else:
                for i, opt in enumerate(node["options"]):
                    if user_input.lower() == opt.lower():
                        choice = i
                        break
                else:
                    print("Please enter a valid option.")
                    continue
                break

        answer = node["options"][choice]
        state["answers"][node["id"]] = answer

        if "signal" in node:
            apply_signal(node["signal"][choice])

        current = next_node(node)

    # ---------- DECISION ----------
    elif node["type"] == "decision":
        next_id = run_decision(node)

        if not next_id:
            print("\n⚠️ No decision rule matched.")
            print("DEBUG axis1:", state["axis1"])
            print("DEBUG axis2:", state["axis2"])
            print("DEBUG axis3:", state["axis3"])
            break

        current = next_id

    # ---------- REFLECTION / BRIDGE ----------
    elif node["type"] in ["reflection", "bridge"]:
        input("\n(Press Enter to continue)")
        current = next_node(node)

    # ---------- SUMMARY ----------
    elif node["type"] == "summary":
        print("\n--- SUMMARY ---")
        input("\n(Press Enter to finish)")
        current = next_node(node)

    # ---------- END ----------
    elif node["type"] == "end":
        print("\nSession complete. See you tomorrow.")
        break

    else:
        print(f"\n⚠️ Unknown node type: {node['type']}")
        break

from google.colab import files
uploaded = files.upload()
