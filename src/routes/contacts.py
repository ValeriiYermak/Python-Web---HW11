from fastapi import APIRouter, Depends, HTTPException, status, Query, Path
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.db import get_db
from src.repository import contacts as repository_contacts
from src.schemas.contacts import ContactResponse, ContactUpdateSchema, \
    ContactSchema
from typing import List, Optional

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=List[ContactResponse],
            response_model_exclude_unset=True)
async def get_contacts(limit: int = Query(default=10, ge=10, le=500),
                       offset: int = Query(default=0, ge=0),
                       query: Optional[str] = None,
                       db: AsyncSession = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(limit, offset, query, db)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: int = Path(ge=1),
                      db: AsyncSession = Depends(get_db)):
    contact = await repository_contacts.get_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Contact not found")
    return contact


@router.post("/", response_model=ContactResponse,
             status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactSchema,
                         db: AsyncSession = Depends(get_db)):
    contact = await repository_contacts.create_contact(body, db)
    return contact


@router.put("/{contact_id}")
async def update_contact(body: ContactUpdateSchema,
                         contact_id: int = Path(ge=1),
                         db: AsyncSession = Depends(get_db)):
    contact = await repository_contacts.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Contact not found")
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int = Path(ge=1),
                         db: AsyncSession = Depends(get_db)):
    contact = await repository_contacts.delete_contact(contact_id, db)
    return contact


@router.get("/birthdays", response_model=List[ContactResponse])
async def get_upcoming_birthdays(db: AsyncSession = Depends(get_db)):
    contacts = await repository_contacts.get_upcoming_birthdays(db)
    return contacts
