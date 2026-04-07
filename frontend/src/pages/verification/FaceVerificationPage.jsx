import { useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

export default function FaceVerificationPage() {
  const navigate = useNavigate();
  const { updateUser } = useAuth();

  const handleVerify = () => {
    // TODO: replace with real webcam + backend verification
    updateUser({ faceVerified: true });
    navigate("/driver/trips");
  };

  return (
    <div style={{ padding: 30 }}>
      <h2>Live Facial Verification</h2>
      <p>Please verify your face before proceeding to trips.</p>
      <button onClick={handleVerify}>Start Verification (Mock)</button>
    </div>
  );
}