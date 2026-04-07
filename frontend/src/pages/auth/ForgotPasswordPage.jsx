import { Link } from "react-router-dom";
import "../../styles/auth.css";

export default function ForgotPasswordPage() {
  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-left">
          <div className="watermark">SR</div>
          <div className="brand-content">
            <h2>SecureRide</h2>
            <p>
              Reset your password securely and continue using your driver account.
            </p>
          </div>
          <div className="left-footer">
            <span>About</span>
            <span>FAQ</span>
            <span>Support</span>
          </div>
        </div>

        <div className="auth-right">
          <h1>Forgot Password</h1>
          <p className="subtitle">
            Enter your email address to receive a password reset link.
          </p>

          <form className="auth-form">
            <div className="field">
              <label>Email Address</label>
              <input type="email" placeholder="you@example.com" />
            </div>

            <button type="submit" className="btn-primary">
              Send Reset Link
            </button>
          </form>

          <p className="switch-auth">
            Back to{" "}
            <Link to="/login" className="auth-link">
              Login
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}