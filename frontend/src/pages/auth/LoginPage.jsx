import { Link } from "react-router-dom";
import "../../styles/auth.css";

export default function LoginPage() {
  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-left">
          <div className="watermark">SR</div>
          <div className="brand-content">
            <h2>SecureRide</h2>
            <p>
              SecureRide helps keep drivers and passengers safe through identity
              verification and smart safety features.
            </p>
          </div>
          <div className="left-footer">
            <span>About</span>
            <span>FAQ</span>
            <span>Support</span>
          </div>
        </div>

        <div className="auth-right">
          <h1>Login</h1>
          <p className="subtitle">Welcome back. Please sign in to continue.</p>

          <form className="auth-form">
            <div className="field">
              <label>Email Address</label>
              <input type="email" placeholder="you@example.com" />
            </div>

            <div className="field">
              <label>Password</label>
              <input type="password" placeholder="••••••••" />
            </div>

            <div className="row-end">
              <Link to="/forgot-password" className="auth-link">
                Forgot Password?
              </Link>
            </div>

            <button type="submit" className="btn-primary">
              Sign In
            </button>
          </form>

          <p className="switch-auth">
            Don’t have an account?{" "}
            <Link to="/register" className="auth-link">
              Register now
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}