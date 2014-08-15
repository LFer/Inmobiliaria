
{
    "name" : "dtm_inmobiliaria",
    "version" : "1.0",
    "author" : "Datamatic",
    "website" : "www.datamatic.com.uy",
    "category" : "Inmobiliarias",
    "description": """ Gestión de Inmobiliarias """,
    "depends" : ['base','crm_claim','project'],
    "init_xml" : ['estate_security.xml'],
    "demo_xml" : [],
    "update_xml" : ['partner_view.xml',
                    'estate_view.xml',
                    'estate_report.xml',
                    'crm_lead_view.xml'],
    "installable": True,
    "active": False,
}
