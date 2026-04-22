import React, { useState } from "react";
import API from "../api";

function AddProduct() {
  const [name, setName] = useState("");
  const [quantity, setQuantity] = useState("");
  const [price, setPrice] = useState("");

  const handleAdd = async () => {
    try {
      await API.post("/products/", {
        name,
        quantity: parseInt(quantity),
        price: parseFloat(price),
     });
      alert("Product Added ✅");
    } catch {
      alert("Error ❌");
    }
  };

  return (
    <div className="bg-white p-4 rounded-xl shadow">
      <h3 className="font-bold mb-2">Add Product</h3>

      <input className="w-full mb-2 p-2 border rounded"
        placeholder="Name"
        onChange={(e) => setName(e.target.value)}
      />

      <input className="w-full mb-2 p-2 border rounded"
        placeholder="Quantity"
        onChange={(e) => setQuantity(e.target.value)}
      />

      <input className="w-full mb-2 p-2 border rounded"
        placeholder="Price"
        onChange={(e) => setPrice(e.target.value)}
      />

      <button
        onClick={handleAdd}
        className="w-full bg-green-500 text-white p-2 rounded hover:bg-green-600"
      >
        Add Product
      </button>
    </div>
  );
}

export default AddProduct;