Title: Designing a Deterministic Reflection Tree for Daily Self-Awareness
1. Why These Questions

The core goal of this system is not to “evaluate” the employee, but to surface latent patterns of thinking in a way that feels natural and non-threatening.

Each axis was translated into observable behaviors, not abstract traits:

Axis 1: Locus (Victim vs Victor)

Instead of asking “Do you take responsibility?”, the tree asks:

“What did you do first?”
“What influenced your response?”

This grounds the abstract concept of agency into specific actions and decisions, making reflection concrete rather than philosophical.

Axis 2: Orientation (Contribution vs Entitlement)

The challenge here was avoiding “correct answer bias.”

Instead of framing entitlement negatively:

“I ensured I upheld my part while others handled theirs”

This captures entitlement as boundary-based reasoning, which is how employees genuinely perceive their behavior. This avoids moral pressure while still surfacing the axis.

Axis 3: Radius (Self → System)

Rather than repeating similar questions, Axis 3 introduces perspective shifts:

“Who did your actions impact?”
“Who would feel it first if delayed?”

This forces the user to simulate downstream effects, expanding awareness from self → team → system.

2. Branching Design & Trade-offs
Early Branching (Axis 1)

The tree introduces a decision node immediately after the opening question:

Productive/Mixed → proactive framing
Frustrating/Draining → reactive framing

Why this matters:
It captures contextual mindset, not just behavior.

Multi-step Evaluation Before Reflection

Instead of branching after one question:

The system collects 2–3 signals first
Then evaluates via a decision node

Trade-off:

Slightly longer flow
But significantly more accurate psychological signal
Deterministic Simplicity vs Expressiveness

The system avoids:

Free text
Scoring models
AI interpretation

Instead uses:

Fixed options
Signal tallies
Rule-based decisions

Trade-off:

Less expressive than LLMs
But fully auditable, consistent, and debuggable
Controlled Redundancy

Some nodes (like parallel paths in Axis 1) are duplicated structurally to preserve:

Deterministic clarity
Easy traceability

This was chosen over abstract routing logic to keep the tree human-readable as data.

3. Psychological Foundations

The design is grounded in three core frameworks:

Locus of Control — Julian Rotter (1954)

Used to distinguish:

Internal → action-oriented responses
External → situational or passive responses

Signals are mapped through behavioral proxies like:

“adjusted approach” vs “waited”
Growth Mindset — Carol Dweck (2006)

Embedded indirectly through:

Adaptation choices
Ownership signals
Response to difficulty
Organizational Citizenship Behavior — Dennis Organ (1988)

Axis 2 reflects:

Contribution beyond role
Initiative vs compliance
Psychological Entitlement — Campbell et al. (2004)

Captured through:

Boundary framing
Expectation of others’ roles
Self-Transcendence — Abraham Maslow (1969)

Axis 3 reflects movement from:

Self → Team → Individual → System

This aligns with Maslow’s expanded hierarchy where meaning comes from contributing beyond self-interest.

Perspective-Taking — Daniel Batson (2011)

Axis 3 questions simulate:

Impact chains
Role-based awareness
4. What I Would Improve With More Time
1. Richer State-Based Personalization

Currently:

Reflections depend on dominant signals

Future:

Combine cross-axis insights:
Example: “High agency + low contribution”
2. More Subtle Option Design

Some options are still slightly distinguishable as “better.”

Improvement:

Make all options equally defensible psychologically
3. Temporal Memory (Multi-day Reflection)

Current system:

Single-day snapshot

Future:

Track trends:
“You’ve leaned external 3 days in a row”
4. Adaptive Depth

Right now:

Fixed depth for all users

Future:

Shallow vs deep paths based on engagement
5. UI Layer

A CLI works, but:

Visual flow
Progress indication
Micro-interactions

would significantly improve engagement.

Final Thought

This system is designed to feel like:

“A structured conversation with a thoughtful peer”

Not:

A test
A diagnosis
A motivational tool

The goal is quiet awareness — helping the user notice patterns in how they:

interpret events (Axis 1)
contribute to others (Axis 2)
relate to the system (Axis 3)

Because once visible, these patterns become changeable.
