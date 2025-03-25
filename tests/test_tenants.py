# tests/test_tenants.py
def test_tenant_isolation(premium_tenant, free_tenant):
    with premium_tenant.db_session() as session:
        session.add(Product(name="Premium"))

    with free_tenant.db_session() as session:
        assert session.query(Product).count() == 0