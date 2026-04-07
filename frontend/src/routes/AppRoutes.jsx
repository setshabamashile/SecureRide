import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import LoginPage from "../pages/auth/LoginPage";
import RegisterPage from "../pages/auth/RegisterPage";
import ForgotPasswordPage from "../pages/auth/ForgotPasswordPage";
import WelcomePage from "../pages/driver/WelcomePage";
import CarDetailsPage from "../pages/driver/CarDetailsPage";
import FaceVerificationPage from "../pages/verification/FaceVerificationPage";
import VerificationConsentPage from "../pages/verification/VerificationConsentPage";
import UploadIdPage from "../pages/verification/UploadIdPage";
import TripsPage from "../pages/driver/TripsPage";
import ProtectedRoute from "./ProtectedRoute";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Public routes */}
        <Route path="/" element={<Navigate to="/login" replace />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/forgot-password" element={<ForgotPasswordPage />} />

        {/* Protected routes */}
        <Route
          path="/welcome"
          element={
            <ProtectedRoute>
              <WelcomePage />
            </ProtectedRoute>
          }
        />

        <Route
          path="/driver/car-details"
          element={
            <ProtectedRoute>
              <CarDetailsPage />
            </ProtectedRoute>
          }
        />

        <Route
          path="/driver/verification-consent"
          element={
            <ProtectedRoute>
              <VerificationConsentPage />
            </ProtectedRoute>
          }
        />

        <Route
          path="/driver/upload-id"
          element={
            <ProtectedRoute>
              <UploadIdPage />
            </ProtectedRoute>
          }
        />

        <Route
          path="/driver/face-verification"
          element={
            <ProtectedRoute>
              <FaceVerificationPage />
            </ProtectedRoute>
          }
        />

        <Route
          path="/driver/trips"
          element={
            <ProtectedRoute>
              <TripsPage />
            </ProtectedRoute>
          }
        />

        {/* Fallback */}
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </BrowserRouter>
  );
}