```mermaid
graph TD
    %% Node Definitions
    START([START: Good evening]) 
    A1_OPEN[A1_OPEN: How was your day?]
    A1_ROUTE{A1_ROUTE: Branching}
    
    %% Axis 1: Locus (Parallel Paths)
    subgraph Axis_1_Locus [Axis 1: Victim vs Victor]
        A1_Q1_H[A1_Q1_HIGH: Response to planning]
        A1_Q2_H[A1_Q2_HIGH: Response to challenge]
        A1_Q3_H[A1_Q3_HIGH: Influence]
        A1_D_H{A1_DECISION_HIGH}

        A1_Q1_L[A1_Q1_LOW: Response to difficulty]
        A1_Q2_L[A1_Q2_LOW: Response to challenge]
        A1_Q3_L[A1_Q3_LOW: Influence]
        A1_D_L{A1_DECISION_LOW}

        A1_R_INT[Reflection: Internal Locus]
        A1_R_EXT[Reflection: External Locus]
        A1_R_MIX[Reflection: Mixed Locus]
    end

    BRIDGE_1_2[[BRIDGE_1_2: Agency to Contribution]]

    %% Axis 2: Orientation (Linear Path to Decision)
    subgraph Axis_2_Orientation [Axis 2: Contribution vs Entitlement]
        A2_Q1[A2_Q1: Interaction approach]
        A2_Q2[A2_Q2: Going beyond]
        A2_Q3[A2_Q3: Source of effort]
        A2_D{A2_DECISION}
        
        A2_R_CON[Reflection: Contribution]
        A2_R_ENT[Reflection: Entitlement]
        A2_R_NEU[Reflection: Neutral]
    end

    BRIDGE_2_3[[BRIDGE_2_3: Broadening the Lens]]

    %% Axis 3: Radius (Linear Path to Decision)
    subgraph Axis_3_Radius [Axis 3: Self-Centrism vs Altrocentrism]
        A3_Q1[A3_Q1: Most central today?]
        A3_Q2[A3_Q2: Who was impacted?]
        A3_D{A3_DECISION}

        A3_R_SYS[Reflection: System Impact]
        A3_R_TEAM[Reflection: Team Impact]
        A3_R_SELF[Reflection: Self Impact]
    end

    SUMMARY[SUMMARY: The Mirror]
    END([END: Session Complete])

    %% Connections
    START --> A1_OPEN
    A1_OPEN --> A1_ROUTE

    %% A1 High Branch
    A1_ROUTE -- "Productive/Mixed" --> A1_Q1_H
    A1_Q1_H --> A1_Q2_H
    A1_Q2_H --> A1_Q3_H
    A1_Q3_H --> A1_D_H
    A1_D_H --> A1_R_INT
    A1_D_H --> A1_R_EXT
    A1_D_H --> A1_R_MIX

    %% A1 Low Branch
    A1_ROUTE -- "Frustrating/Draining" --> A1_Q1_L
    A1_Q1_L --> A1_Q2_L
    A1_Q2_L --> A1_Q3_L
    A1_Q3_L --> A1_D_L
    A1_D_L --> A1_R_INT
    A1_D_L --> A1_R_EXT
    A1_D_L --> A1_R_MIX

    %% Transitions to A2
    A1_R_INT & A1_R_EXT & A1_R_MIX --> BRIDGE_1_2
    BRIDGE_1_2 --> A2_Q1
    
    %% A2 Flow
    A2_Q1 --> A2_Q2
    A2_Q2 --> A2_Q3
    A2_Q3 --> A2_D
    A2_D --> A2_R_CON
    A2_D --> A2_R_ENT
    A2_D --> A2_R_NEU

    %% Transitions to A3
    A2_R_CON & A2_R_ENT & A2_R_NEU --> BRIDGE_2_3
    BRIDGE_2_3 --> A3_Q1

    %% A3 Flow
    A3_Q1 --> A3_Q2
    A3_Q2 --> A3_D
    A3_D --> A3_R_SYS
    A3_D --> A3_R_TEAM
    A3_D --> A3_R_SELF

    %% Exit Flow
    A3_R_SYS & A3_R_TEAM & A3_R_SELF --> SUMMARY
    SUMMARY --> END

    %% Styling
    style A1_ROUTE fill:#f9f,stroke:#333,stroke-width:2px
    style A2_D fill:#f9f,stroke:#333,stroke-width:2px
    style A3_D fill:#f9f,stroke:#333,stroke-width:2px
    style BRIDGE_1_2 fill:#bbf,stroke:#333,stroke-dasharray: 5 5
    style BRIDGE_2_3 fill:#bbf,stroke:#333,stroke-dasharray: 5 5
