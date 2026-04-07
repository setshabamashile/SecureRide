import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

export default function CarDetailsPage() {
  const navigate = useNavigate();
  const { user, updateUser } = useAuth();

  const [car, setCar] = useState({
    make: "",
    model: "",
    year: "",
    plateNumber: "",
    color: "",
  });

  const handleChange = (e) => {
    setCar((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    updateUser({
      carDetailsCompleted: true,
      carDetails: car,
    });

    navigate("/driver/face-verification");
  };

  if (!user) return null;

  return (
    <div style={{ padding: 30 }}>
      <h2>Driver Car Details</h2>
      <form onSubmit={handleSubmit} style={{ maxWidth: 420, display: "grid", gap: 10 }}>
        <input name="make" placeholder="Car Make (Toyota)" onChange={handleChange} required />
        <input name="model" placeholder="Car Model (Corolla)" onChange={handleChange} required />
        <input name="year" placeholder="Year (2020)" onChange={handleChange} required />
        <input name="plateNumber" placeholder="Plate Number" onChange={handleChange} required />
        <input name="color" placeholder="Color" onChange={handleChange} required />
        <button type="submit">Save Car Details</button>
      </form>
    </div>
  );
}