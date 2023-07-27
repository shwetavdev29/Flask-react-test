import React, { useState } from "react";

const TodoList = () => {
  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState("");

  const addItem = () => {
    if (newItem.trim() !== "") {
      setItems([...items, newItem.trim()]);
      setNewItem("");
    }
  };

  const deleteItem = (index) => {
    const updatedItems = [...items];
    updatedItems.splice(index, 1);
    setItems(updatedItems);
  };

  return (
    <div>
      <h1>To-Do List</h1>
      <div>
        <input
          type="text"
          value={newItem}
          onChange={(e) => setNewItem(e.target.value)}
          style={{
            fontFamily: "sans-serif",
            fontSize: "20px"
          }}
        />
        <button
          style={{
            fontFamily: "sans-serif",
            fontSize: "20px",
            color: "white",
            backgroundColor: "green",
            borderRadius: "5px",
            borderColor: "green"
          }}
          onClick={addItem}
        >
          Add
        </button>
      </div>
      <ul>
        {items.map((item, index) => (
          <li
            key={index}
            style={{
              fontFamily: "sans-serif",
              fontSize: "20px"
            }}
          >
            <span style={{ paddingRight: "15px" }}>{item}</span>
            <button
              style={{
                fontFamily: "sans-serif",
                fontSize: "20px",
                color: "white",
                backgroundColor: "red",
                borderRadius: "5px",
                borderColor: "red"
              }}
              onClick={() => deleteItem(index)}
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoList;