from Utils.db import db
from Models.models import ItemsModel, GraphData


#####################################################################################
async def get_items():
    query = "SELECT * FROM items"
    rows = await db.fetch(query)
    return {"items": rows}
################################################
async def create_items(items: ItemsModel):

    query = ("INSERT INTO items(name, category, quantity, createdOn) "
             "VALUES($1, $2, $3, CURRENT_TIMESTAMP) "
             "RETURNING *;")

    row = await db.fetch(query, items.name,items.category,items.quantity)

    return {"message": "User created successfully", "item": row}
#############################################################################
async def delete_items(item_id: int):
    await db.execute(
        "DELETE FROM items WHERE id = $1 RETURNING id", item_id
    )
    return {"message": "User has been deleted successfully."}
################################################################################
async def get_categories_total():
    query = """
    SELECT category, SUM(quantity) AS quantity
    FROM items
    GROUP BY category
    """
    rows = await db.fetch(query)

    category_data = {row[0]: row[1] for row in rows}
    labels = ["food","clothes","medicine","household"]
    values = []

    for category in labels:
        quantity = category_data.get(category, 0)
        values.append(quantity)

    return GraphData(labels=labels, values=values)