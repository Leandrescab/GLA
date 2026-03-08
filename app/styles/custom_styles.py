import streamlit as st


def inject_global_css():
    """Inyecta todos los estilos CSS personalizados para la aplicación."""
    custom_css = """
    <style>

    /* ─────────────────────────────────────────────
       BACKGROUND & GLOBAL
    ───────────────────────────────────────────── */
    [data-testid="stAppViewContainer"] {
        /* Gradiente dinámico: usa el fondo del tema y una variante secundaria */
        background: linear-gradient(to bottom, var(--background-color) 0%, var(--secondary-background-color) 100%);
        background-attachment: fixed;
        color: var(--text-color);
    }

    code, pre, .banner-path {
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* ─────────────────────────────────────────────
       SIDEBAR
    ───────────────────────────────────────────── */
    [data-testid="stSidebar"] {
        background-color: var(--background-color);
        border-right: 1px solid rgba(128, 128, 128, 0.2);
    }

    /* ─────────────────────────────────────────────
       EXPANDER & DATA EDITOR
    ───────────────────────────────────────────── */
    [data-testid="stExpander"], [data-testid="stDataEditor"] {
        border: 1px solid rgba(128, 128, 128, 0.2) !important;
        border-radius: 14px !important;
    }

    /* ─────────────────────────────────────────────
       PANEL HEADER
    ───────────────────────────────────────────── */
    .panel-head {
        /* Color primario con transparencia para adaptarse al fondo */
        background: rgba(56, 139, 253, 0.1); 
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-left: 3px solid var(--primary-color);
        border-radius: 14px;
        padding: 14px 18px;
        margin-bottom: 15px;
        animation: fadeSlideIn 0.25s cubic-bezier(0.16, 1, 0.3, 1) both;
    }

    .panel-head-row {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 1px;
    }

    .panel-head-icon { font-size: 18px; }
    .panel-head-caption { 
        font-size: 14px; 
        color: var(--text-color); 
        opacity: 0.8; 
    }

    /* ─────────────────────────────────────────────
       BADGE
    ───────────────────────────────────────────── */
    .panel-badge {
        display: inline-flex;
        align-items: center;
        gap: 3px;
        padding: 4px 10px;
        background: rgba(56, 139, 253, 0.15);
        border: 1px solid var(--primary-color);
        border-radius: 20px;
        font-size: 10px;
        font-weight: 600;
        color: var(--primary-color);
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }

    /* ─────────────────────────────────────────────
       ANIMATION
    ───────────────────────────────────────────── */
    @keyframes fadeSlideIn {
        from { opacity: 0; transform: translateY(6px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    /* ─────────────────────────────────────────────
       SAVE BANNER SUCCESS
    ───────────────────────────────────────────── */
    .save-banner-ok {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 14px 18px;
        background: rgba(63, 185, 80, 0.1);
        border: 1px solid rgba(63, 185, 80, 0.3);
        border-left: 3px solid #3fb950;
        border-radius: 10px;
        color: #3fb950;
        margin-top: 16px;
    }

    .save-banner-ok .banner-path {
        font-size: 11px;
        color: var(--text-color);
        opacity: 0.6;
        margin-top: 2px;
    }


    /* ─────────────────────────────────────────────
       SAVE BANNER WARNING
    ───────────────────────────────────────────── */
    .banner-warning {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 14px 18px;
        background: rgba(255, 193, 7, 0.1);
        border: 1px solid rgba(255, 193, 7, 0.3);
        border-left: 3px solid #ffc107;
        border-radius: 10px;
        color: #ffc107;
        margin-top: 16px;
    }

    .banner-warning .banner-warning-text {
        font-size: 11px;
        color: var(--text-color);
        opacity: 0.6;
        margin-top: 2px;
    }

    /* ─────────────────────────────────────────────
       FANCY PRIMARY BUTTON
    ───────────────────────────────────────────── */
    div[data-testid="stButton"] button[kind="primary"] {
        display: block !important;
        margin: 0 auto !important;
        width: 100%;
        background: rgba(56, 139, 253, 0.1);
        border: 1px solid var(--primary-color) !important;
        color: var(--primary-color) !important;
        font-size: 10px;
        padding: 3px 10px;
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.25s ease;
    }

    div[data-testid="stButton"] button[kind="primary"]:hover {
        transform: translateY(-2px);
        background: var(--primary-color);
        color: white !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }


    /* ─────────────────────────────────────────────
       METRIC CARDS
    ───────────────────────────────────────────── */
    /* general style for the metric container */
    .metric-card {
        background-color: #1a1e26; /* background color */
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        height: 100%; /* all cards have the same height */
    }
    /* style for the metric title */
    .metric-title {
        color: #9AA0A6; /* text color */
        font-size: 14px;
        margin-bottom: 5px;
        font-weight: 500;
    }
    /* style for the metric value */
    .metric-value {
        color: #FFFFFF; /* text color */
        font-size: 28px;
        font-weight: 700;
        line-height: 1.2;
    }
    /* style for the metric unit */
    .metric-unit {
        font-size: 18px;
        color: #9AA0A6;
    }
    /* style for the metric status tag */
    .status-tag {
        font-size: 14px;
        font-weight: 600;
        margin-top: 10px;
        color: #00E676; /* text color */
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)