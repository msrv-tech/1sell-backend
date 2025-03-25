# app/middleware/tenant.py
from fastapi import Request, HTTPException


async def tenant_middleware(request: Request, call_next):
    tenant_id = get_tenant_from_request(request)  # Из поддомена/JWT
    if is_premium(tenant_id):
        request.state.db_url = get_premium_db_url(tenant_id)
    else:
        request.state.db_url = get_shared_db_url(tenant_id)

    response = await call_next(request)
    return response