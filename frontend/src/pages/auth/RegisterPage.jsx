import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import "../../styles/auth.css";

export default function RegisterPage() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    fullNames: "",
    idNumber: "",
    gender: "",
    race: "",
    accountType: "",
    address: "",
    email: "",
    contactNumber: "",
    password: "",
    confirmPassword: "",
  });

  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault(); // stops page refresh/clearing
    setError("");

    if (formData.password !== formData.confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    // TODO: send to backend API here
    // await axios.post("/api/register", formData)

    // Simulate success and redirect to login
    navigate("/login");
  };

  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-left">
          <div className="watermark">SR</div>
          <div className="brand-content">
            <h2>SecureRide</h2>
            <p>Create your verified account using your official personal details.</p>
          </div>
          <div className="left-footer">
            <span>About</span><span>FAQ</span><span>Support</span>
          </div>
        </div>

        <div className="auth-right">
          <h1>Create Account</h1>
          <p className="subtitle">Fill in your details to register.</p>

          <form className="auth-form" onSubmit={handleSubmit}>
            <div className="field">
              <label>Full Names (as per ID)</label>
              <input name="fullNames" value={formData.fullNames} onChange={handleChange} type="text" required />
            </div>

            <div className="field">
              <label>ID Number</label>
              <input name="idNumber" value={formData.idNumber} onChange={handleChange} type="text" required />
            </div>

            <div className="field">
              <label>Gender</label>
              <select name="gender" value={formData.gender} onChange={handleChange} required>
                <option value="">Select gender</option>
                <option value="female">Female</option>
                <option value="male">Male</option>
              </select>
            </div>

            <div className="field">
              <label>Race</label>
              <select name="race" value={formData.race} onChange={handleChange} required>
                <option value="">Select race</option>
                <option value="african">African</option>
                <option value="coloured">Coloured</option>
                <option value="indian_asian">Indian / Asian</option>
                <option value="white">White</option>
                <option value="other">Other</option>
              </select>
            </div>

            <div className="field">
              <label>Account Type</label>
              <select name="accountType" value={formData.accountType} onChange={handleChange} required>
                <option value="">Select account type</option>
                <option value="driver">Driver</option>
                <option value="passenger">Passenger</option>
              </select>
            </div>

            <div className="field">
              <label>Address</label>
              <input name="address" value={formData.address} onChange={handleChange} type="text" required />
            </div>

            <div className="field">
              <label>Email Address</label>
              <input name="email" value={formData.email} onChange={handleChange} type="email" required />
            </div>

            <div className="field">
              <label>Contact Number</label>
              <input name="contactNumber" value={formData.contactNumber} onChange={handleChange} type="tel" required />
            </div>

            <div className="field">
              <label>Create Password</label>
              <input name="password" value={formData.password} onChange={handleChange} type="password" required />
            </div>

            <div className="field">
              <label>Confirm Password</label>
              <input name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} type="password" required />
            </div>

            {error && <p style={{ color: "red", fontSize: "13px" }}>{error}</p>}

            <button type="submit" className="btn-primary">Register</button>
          </form>

          <p className="switch-auth">
            Already have an account? <Link to="/login" className="auth-link">Login</Link>
          </p>
        </div>
      </div>
    </div>
  );
}