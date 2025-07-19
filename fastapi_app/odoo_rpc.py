import os
import xmlrpc.client

ODOO_URL = os.getenv("ODOO_URL")
ODOO_DB = os.getenv("ODOO_DB")
ODOO_USER = os.getenv("ODOO_USER")
ODOO_PASSWORD = os.getenv("ODOO_PASSWORD")

class OdooConnector:

    def __init__(self):
        if not ODOO_URL:
            raise Exception("❌ ODOO_URL no está definido.")
        self.common = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/common")
        self.uid = self.common.authenticate(
            os.getenv("ODOO_DB"),
            os.getenv("ODOO_USER"),
            os.getenv("ODOO_PASSWORD"),
            {}
        )
        self.models = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/object")


    def get_partners(self, limit=10):
        return self.models.execute_kw(
            ODOO_DB,
            self.uid,
            ODOO_PASSWORD,
            'res.partner',
            'search_read',
            [[['is_company', '=', True]]],
            {'fields': ['id', 'name', 'email'], 'limit': limit}
        )
