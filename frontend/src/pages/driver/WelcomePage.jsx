import { useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import "../../styles/welcome.css";

export default function WelcomePage() {
  const navigate = useNavigate();
  const { user, logout } = useAuth();

  if (!user) return null;

  const goNext = () => {
    if (user.accountType !== "driver") {
      navigate("/driver/trips");
      return;
    }

    if (!user.carDetailsCompleted) {
      navigate("/driver/car-details");
      return;
    }

    if (!user.idDocumentUploaded) {
      navigate("/driver/verification-consent");
      return;
    }

    if (!user.faceVerified) {
      navigate("/driver/face-verification");
      return;
    }

    navigate("/driver/trips");
  };

  return (
    <div className="welcome-page">
      <div className="welcome-card">
        <div className="welcome-arc left" />
        <div className="welcome-arc right" />

        <div className="welcome-chip">SecureRide Driver Verification</div>

        <h1 className="welcome-title">
          Welcome, {user.fullNames || "Driver"} <span>👋</span>
        </h1>

        <p className="welcome-subtitle">
          Complete your setup to continue to the trips section.
        </p>

        <div className="welcome-status-list">
          <div className="welcome-status-item">
            <span>Account Type:</span>
            <strong>{user.accountType || "—"}</strong>
          </div>

          <div className="welcome-status-item">
            <span>Car details:</span>
            <strong>{user.carDetailsCompleted ? "✅ Complete" : "❌ Not complete"}</strong>
          </div>

          <div className="welcome-status-item">
            <span>ID upload:</span>
            <strong>{user.idDocumentUploaded ? "✅ Uploaded" : "❌ Not uploaded"}</strong>
          </div>

          <div className="welcome-status-item">
            <span>Facial verification:</span>
            <strong>{user.faceVerified ? "✅ Verified" : "❌ Not verified"}</strong>
          </div>
        </div>

        <div className="welcome-actions">
          <button className="welcome-btn primary" onClick={goNext}>
            Continue
          </button>
          <button className="welcome-btn ghost" onClick={logout}>
            Logout
          </button>
        </div>
      </div>
    </div>
  );
}