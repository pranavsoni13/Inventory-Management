import React from "react";
import AddProduct from "../components/AddProduct";
import ProductList from "../components/ProductList";

function Dashboard() {
  const logout = () => {
    localStorage.removeItem("token");
    window.location.href = "/";
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Navbar */}
      <div className="bg-blue-600 text-white p-4 flex justify-between">
        <h1 className="font-bold">Inventory Dashboard</h1>
        <button onClick={logout} className="bg-red-500 px-3 py-1 rounded">
          Logout
        </button>
      </div>

      {/* Content */}
      <div className="p-6 grid grid-cols-2 gap-4">
        <AddProduct />
        <ProductList />
      </div>
    </div>
  );
}

export default Dashboard;