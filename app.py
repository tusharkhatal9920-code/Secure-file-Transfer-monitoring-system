import streamlit as st
import hashlib
import os

st.set_page_config(
    page_title="Secure File Transfer Monitoring System",
    page_icon="🔐"
)

st.title("🔐 Secure File Transfer Monitoring System")
st.write("File monitoring, SHA-256 integrity verification and sensitive file detection.")

st.header("1. Upload File")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:

    data = uploaded_file.read()

    # SHA-256
    sha256 = hashlib.sha256(data).hexdigest()

    st.success("File uploaded successfully!")

    st.write("### File Information")
    st.write("**File Name:**", uploaded_file.name)
    st.write("**File Size:**", len(data), "bytes")

    st.write("### SHA-256 Hash")
    st.code(sha256)

    # Sensitive file detection
    sensitive_words = [
        "password",
        "confidential",
        "secret",
        "salary",
        "private",
        "financial",
        "restricted"
    ]

    filename = uploaded_file.name.lower()

    sensitive = any(word in filename for word in sensitive_words)

    st.write("### Security Status")

    if sensitive:
        st.error("⚠️ WARNING: Sensitive File Detected")
    else:
        st.success("✅ Normal File")

    st.header("2. Integrity Verification")

    second_file = st.file_uploader(
        "Upload the same file again to compare its integrity",
        key="second"
    )

    if second_file is not None:

        second_hash = hashlib.sha256(
            second_file.read()
        ).hexdigest()

        if sha256 == second_hash:
            st.success("✅ Integrity Verified — Hashes Match")
        else:
            st.error("🚨 SECURITY ALERT — File Integrity Violation")
            st.write("Original Hash:")
            st.code(sha256)
            st.write("New Hash:")
            st.code(second_hash)

st.divider()

st.header("Project Features")

st.write("✅ File Transfer Monitoring")
st.write("✅ Sensitive File Detection")
st.write("✅ SHA-256 Integrity Verification")
st.write("✅ Security Alert Generation")
st.write("✅ Audit and Security Monitoring")
