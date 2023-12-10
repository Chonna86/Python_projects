import argparse
from models import Student, Group, Teacher, Subject, Grade
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:password@localhost/postgres')
Session = sessionmaker(bind=engine)
session = Session()

def create_record(model, **kwargs):
    try:
        # Creating a new record
        new_record = model(**kwargs)
        session.add(new_record)
        session.commit()
        return f"Record created successfully: {new_record}"
    except Exception as e:
        session.rollback()
        return f"Error creating record: {e}"

def list_records(model):
    try:
        # Listing all records
        records = session.query(model).all()
        return records
    except Exception as e:
        return f"Error listing records: {e}"

def update_record(model, record_id, **kwargs):
    try:
        # Updating a record
        record = session.query(model).filter_by(id=record_id).first()
        if record:
            for key, value in kwargs.items():
                setattr(record, key, value)
            session.commit()
            return f"Record updated successfully: {record}"
        else:
            return f"Record not found with ID: {record_id}"
    except Exception as e:
        session.rollback()
        return f"Error updating record: {e}"

def remove_record(model, record_id):
    try:
        # Removing a record
        record = session.query(model).filter_by(id=record_id).first()
        if record:
            session.delete(record)
            session.commit()
            return f"Record removed successfully: {record}"
        else:
            return f"Record not found with ID: {record_id}"
    except Exception as e:
        session.rollback()
        return f"Error removing record: {e}"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Perform CRUD operations on the database.')
    parser.add_argument('--action', '-a', help='Action: create, list, update, remove', required=True)
    parser.add_argument('--model', '-m', help='Model: Student, Group, Teacher, Subject, Grade', required=True)

    args = parser.parse_args()

    if args.action == 'create':
        create_record(args.model)
    elif args.action == 'list':
        list_records(args.model)
    elif args.action == 'update':
        update_record(args.model)
    elif args.action == 'remove':
        remove_record(args.model)
    else:
        print('Invalid action. Use create, list, update, or remove.')