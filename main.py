import json

def generate_power_platform_doc(app_data):
    """
    Generates a simplified Markdown documentation for a Power Platform application.
    This function simulates the core idea of a "Documentation Generator"
    by taking structured application data and formatting it into a human-readable document.
    """
    doc_lines = []

    # Application Overview
    doc_lines.append(f"# {app_data['name']} Documentation")
    doc_lines.append(f"\n**Type:** {app_data['type']}")
    doc_lines.append(f"**Version:** {app_data['version']}")
    doc_lines.append(f"\n## Description")
    doc_lines.append(app_data['description'])

    # Business Logic
    doc_lines.append(f"\n## Business Logic Summary")
    doc_lines.append(app_data['business_logic_summary'])

    # Components
    doc_lines.append(f"\n## Components")
    if app_data.get('components'):
        for component in app_data['components']:
            doc_lines.append(f"- **{component['name']}** ({component['type']}): {component['purpose']}")
    else:
        doc_lines.append("No specific components listed.")

    # Dependencies
    doc_lines.append(f"\n## Dependencies")
    if app_data.get('dependencies'):
        for dep in app_data['dependencies']:
            doc_lines.append(f"- {dep}")
    else:
        doc_lines.append("No external dependencies listed.")

    return "\n".join(doc_lines)

# --- Example Power Platform Application Definition ---
# This dictionary represents a simplified structure of a Power Platform application
# that a documentation generator might process. It includes key metadata and components.
power_app_example = {
    "name": "Customer Onboarding Portal",
    "description": "A Power Apps portal for new customer registration and initial data collection. Integrates with Power Automate for workflow automation and data storage.",
    "type": "Power Apps Canvas App",
    "version": "1.0.0",
    "components": [
        {"name": "WelcomeScreen", "type": "Screen", "purpose": "Displays initial greeting and login options."},
        {"name": "CustomerInfoForm", "type": "Screen", "purpose": "Collects customer personal and contact details."},
        {"name": "SubmitCustomerDataFlow", "type": "Power Automate Flow", "purpose": "Saves customer data to Dataverse and sends welcome email."},
        {"name": "AdminDashboard", "type": "Screen", "purpose": "Internal screen for admin to review pending applications."}
    ],
    "dependencies": ["Dataverse", "Outlook 365 Connector", "Azure AD"],
    "business_logic_summary": "New customers fill out a form, which triggers an approval workflow and data storage in Dataverse. Admins can monitor progress via a dedicated screen and manage approvals."
}

if __name__ == "__main__":
    print("--- Generating Documentation for Power Platform Application ---")
    documentation_output = generate_power_platform_doc(power_app_example)

    print("\n--- Generated Markdown Documentation ---")
    print(documentation_output)

    # The generated documentation can be saved to a file, e.g., a Markdown file:
    # with open("CustomerOnboardingPortal_Doc.md", "w", encoding="utf-8") as f:
    #     f.write(documentation_output)
    # print("\nDocumentation saved to CustomerOnboardingPortal_Doc.md")
