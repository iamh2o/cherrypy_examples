
gantt
    title LSMC Seed → CLIA Certification (high level)
    dateFormat  YYYY-MM-DD
    excludes    weekends
    section Financing & Governance
    Seed funds closed                        :milestone, seed, 2025-10-15, 1d
    Board cadence + audit committee          :active, board, 2025-10-16, 2026-05-01

    section Hiring & Org
    CEO in seat                              :done, 2025-10-01, 10d
    Founder ops lead (clinical product)      :active, 2025-10-10, 2026-03-31
    Head, Lab Platform R&D (Sandra)          :milestone, 2025-11-01, 1d
    Head, Automation (John W)                :done, 2025-10-01, 1d
    Fractional CISO / Cloud Arch             :ciso, 2025-11-15, 2026-04-30
    Quality Director (CLIA/CAP)              :qdir, 2026-01-15, 2026-06-30
    Lab Director (CLIA CA & NYC)             :labdir, 2026-02-01, 2026-08-31
    HR/People Ops (fractional→FT)            :hr, 2026-02-01, 2026-07-31

    section Facility & Safety
    Lease & TI design                        :ti1, 2025-11-15, 2026-01-31
    Buildout & utilities (power, HVAC)       :ti2, 2026-02-01, 2026-04-15
    EH&S programs (BBP, CHP, training)       :ehs, 2026-03-01, 2026-05-15

    section QMS / CAP / CLIA
    Qms selection & SOP skeleton             :qms1, 2025-12-01, 2026-02-29
    Document control + training system live  :qms2, 2026-03-01, 2026-04-15
    Validation master plan (VMP)             :vmp, 2026-03-01, 2026-04-15
    CLIA application draft                   :clia1, 2026-04-01, 2026-05-01
    CAP self-inspection & gap close          :cap1, 2026-04-15, 2026-06-15
    CLIA inspection window                   :milestone, clia2, 2026-06-30, 1d

    section Instrumentation & Automation
    Illumina bring-up (sequencers + ancill.) :illu, 2026-02-15, 2026-04-15
    Liquid handlers + QC rigs (phase 1)      :auto1, 2026-03-01, 2026-05-15
    Ultima / ONT / PacBio scouting & POC     :multi1, 2026-04-01, 2026-06-30

    section Informatics & LIMS
    LIMS MVP (accession→report)              :lims1, 2025-12-15, 2026-03-31
    Pipeline v1 (GQV metrics, cost telemetry):pipe1, 2026-01-15, 2026-04-30
    Secure cloud posture (IaC, CI/CD, SIEM)  :sec1, 2026-02-01, 2026-05-31
    CLEP-aware validations (NY add-ons)      :clep, 2026-05-01, 2026-08-31

    section Verification & Launch
    End-to-end validation (IQ/OQ/PQ)         :val, 2026-04-15, 2026-06-15
    Pricing & SLOs finalized                 :price, 2026-05-01, 2026-06-01
    CLIA go-live                             :milestone, launch, 2026-07-01, 1d