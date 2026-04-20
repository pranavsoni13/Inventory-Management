import React, { useEffect, useState } from "react";
import API from "../api";

function ProductList() {
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    try {
      const res = await API.get("/products/");
      setProducts(res.data);
    } catch {
      alert("Error loading products");
    }
  };

  const deleteProduct = async (id) => {
    try {
      await API.delete(`/products/${id}`);
      fetchProducts();
    } catch {
      alert("Delete failed");
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <div className="bg-white p-4 rounded-xl shadow">
      <h3 className="font-bold mb-2">Products</h3>

      {products.map((p) => (
        <div key={p.id} className="border p-2 rounded mb-2 flex justify-between">
          <div>
            <p className="font-semibold">{p.name}</p>
            <p className="text-sm">Qty: {p.quantity}</p>
          </div>

          <div className="flex gap-2">
            <p className="text-green-600 font-bold">₹{p.price}</p>
            <button
              onClick={() => deleteProduct(p.id)}
              className="bg-red-500 text-white px-2 rounded"
            >
              Delete
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}

export default ProductList;