from fastapi import FastAPI, Response, Depends, HTTPException, status
import pathlib, csv, os
import uvicorn
from sqlalchemy import select
from schema import People as SchemaP
from models import People as ModelP
from schema import DbUpdateRequest as SchemaU
from typing import List, Union
from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv
from uuid import uuid4, UUID
import uuid


load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

# Load data from file if it doesn't exit in databse
@app.on_event("startup")
def startup_event():
    with db():
        db.session.query(ModelP).first()
        get_passenger = db.session.query(ModelP).first()
        # Load data if there's no results
        if get_passenger is None:
            DATAFILE = pathlib.Path() / 'data' / 'titanic.csv'
            with open(DATAFILE, 'r') as f:
                csv_data = csv.reader(f)
                next(csv.reader(f), None)
                
                for i in csv_data:
                    record = ModelP(**{
                        'uuid' : uuid.uuid4(),
                        'Survived' : i[0],
                        'Pclass' : i[1],
                        'Name' : i[2],
                        'Sex' : i[3],
                        'Age' : i[4],
                        'Siblings_Spouses_Aboard': i[5],
                        'Parents_Children_Aboard': i[6],
                        'Fare' : i[7]
                    })
                    db.session.add(record)
            db.session.commit()

        db.session.close()

# get all passenger
@app.get("/people/")
def get_a_list_of_all_persons():
    people = db.session.query(ModelP).all()
    return people

# get specific person using uuid
@app.get("/people/{uuid}", response_model=SchemaP)
def get_info_about_one_person_by_id(uuid: str):
    person = db.session.query(ModelP).filter(ModelP.uuid == uuid).first()
    if person is None:
        raise HTTPException(
        status_code=404,
        detail= f"person with Id: {uuid} does not exist"
        )
    return person

# get specific person using name
@app.get("/people/person/{FullName}", response_model=SchemaP)
def get_person_by_name(FullName: str):
    FullName = db.session.query(ModelP).filter(ModelP.Name==FullName).first()
    if FullName is None:
        raise HTTPException(
        status_code=404,
        detail= f"person with name: {FullName} does not exist"
        )
    return FullName

# add a person to the database
@app.post("/people/", response_model=SchemaP, status_code=201)
def add_a_person_to_the_database(titanic: SchemaP):
    with db():
        db.session.query(ModelP)
        db_person = ModelP(
            uuid=uuid4(),
            Name=titanic.Name,
            Survived=titanic.Survived,
            Pclass=titanic.Pclass,
            Sex=titanic.Sex,
            Age=titanic.Age,
            Siblings_Spouses_Aboard=titanic.Siblings_Spouses_Aboard,
            Parents_Children_Aboard=titanic.Parents_Children_Aboard,
            Fare=titanic.Fare
            )
        db.session.add(db_person)
        db.session.commit()
        db.session.refresh(db_person)
        db.session.close()
    return db_person

# update database by uuid
@app.put("/people/{uuid}", response_model = SchemaP)
def update_info_about_one_person(update_db: SchemaU, uuid: str):
    with db():
        db.session.query(ModelP)
        db_person = db.session.query(ModelP).filter(ModelP.uuid == uuid).first()
        if not db_person:
            raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'No person with this id: {uuid} found')
        if update_db.Name is not None:
            db_person.Name = update_db.Name
        if update_db.Survived is not None:
            db_person.Survived = update_db.Survived
        if update_db.Pclass is not None:
            db_person.Pclass = update_db.Pclass
        if update_db.Sex is not None:
           db_person.Sex = update_db.Sex
        if update_db.Age is not None:
            db_person.Age = update_db.Age
        if update_db.Parents_Children_Aboard is not None:
            db_person.Parents_children_Aboard = update_db.Parents_Children_Aboard
        if update_db.Siblings_Spouses_Aboard is not None:
            db_person.Siblings_spouses_Aboard = update_db.Siblings_Spouses_Aboard
        if update_db.Fare is not None:
           db_person.Fare = update_db.Fare
        db.session.commit()
        db.session.refresh(db_person)
        db.session.close()
    return db_person

# remove person from database
@app.delete("/people/{uuid}")
def remove_a_person_from_the_database(uuid: str):
    with db():
        person = db.session.query(ModelP).filter(ModelP.uuid == uuid).first()
        db.session.delete(person)
        db.session.commit()
        db.session.close()
        return f"Record with uuid {uuid} successfully removed!"





