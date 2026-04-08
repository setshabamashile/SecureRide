import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import { useAuth } from "../../context/AuthContext";
import "../../styles/auth.css";

export default function LoginPage() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    // MOCK login (replace with backend call)
    const stored = localStorage.getItem("registeredUser");
    if (!stored) {
      alert("No registered user found. Please register first.");
      return;
    }

    const registeredUser = JSON.parse(stored);
    if (registeredUser.email !== email || registeredUser.password !== password) {
      alert("Invalid email or password");
      return;
    }

    login(registeredUser);
    navigate("/welcome");
  };

  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-left">
          <div className="watermark">SR</div>
          <div className="brand-content">
            <h2>SecureRide</h2>
            <p>Driver safety and verification platform.</p>
          </div>
          <div className="left-footer">
            <span>About</span><span>FAQ</span><span>Support</span>
          </div>
        </div>

        <div className="auth-right">
          <h1>Login</h1>
          <p className="subtitle">Welcome back. Please sign in to continue.</p>

          <form className="auth-form" onSubmit={handleSubmit}>
            <div className="field">
              <label>Email Address</label>
              <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
            </div>

            <div className="field">
              <label>Password</label>
              <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
            </div>

            <div className="row-end">
              <Link to="/forgot-password" className="auth-link">Forgot Password?</Link>
            </div>

            <button type="submit" className="btn-primary">Sign In</button>
          </form>

          <p className="switch-auth">
            Don’t have an account? <Link to="/register" className="auth-link">Register now</Link>
          </p>
        </div>
      </div>
    </div>
  );
}