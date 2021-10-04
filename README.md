# satis.ai
## About the problem
**Context**: A multi branch burger that receives different orders

**Problem**: Creation of a process that from a chain of orders and kitchen 
parameters (such as capacity to cook hamburgers in parallel, cooking time, 
packing capacity, packing time, ...) returns the path more optimal for cooking, 
assembly and packaging of orders.

**Main difficult**: Simulate a time task queue with different types of workers

### INPUT
Types of row: 2
```
<restautant_id>, <cooking_capacity>, <cooking_time>, <assembling_capacity>, <assembling_time>, <package_capacity>, <package_time>, <Patties inventory>,<Lettuce inventory>,<Tomato inventory>,<Veggie patties inventory>,<Bacon Inventory>
R1,4C,1,3A,2,2P,1,100,200,200,100,100
<restaurant_id>, <order_time>, <order_id>, [<burguer>, ...]
R1,2020-12-08 19:15:31,O1,BLT,LT,VLT
R1,2020-12-08 19:15:32,O2,VLT,VT,BLT,LT,VLT
...
```
Ingredients:
- L for Lettuce
- T for Tomatoes
- V for Veggie burger
- B for Bacon

Burguers are made with 1 patty.
### OUTPUT

Types of row: 3

```
<Restaurant ID>,<Order ID>,<Accepted or Rejected>,<expected processing time in minutes>
R1,O1,ACCEPTED,8
R1,O2,ACCEPTED,7
R1,O3,REJECTED
<Restaurant ID>,TOTAL,<Total time it takes to process all orders>
R1,TOTAL,25
<Restaurant ID>,Inventory,<Patties inventory>,<Lettuce inventory>,<Tomato inventory>,<Veggie patties inventory>,<Bacon Inventory>
R1,INVENTORY,58,130,115,63,50
```
