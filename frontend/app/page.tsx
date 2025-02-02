import 'bootstrap/dist/css/bootstrap.min.css';
import PatientInfo from "../components/PatientInfo";
import HeartbeatTracking from "../components/HeartbeatTracking";
import FacialExpressionTracking from "../components/FacialExpressionTracking";
import SpeechPatternTracking from "../components/SpeechPatternTracking";
import styles from "./page.module.css";

export default function Home() {
  return (
      <div className="mx-3 mt-3">
        <h1 className="text-center mb-4">Patient Monitoring Dashboard</h1>
  
        {/* Row 1 */}
        <div className="d-flex flex-column flex-md-row m-3">
          <PatientInfo />
          <HeartbeatTracking />
        </div>
  
        {/* Row 2 */}
        <div className="d-flex flex-column flex-md-row m-3">
          <FacialExpressionTracking />
          <SpeechPatternTracking />
        </div>
      </div>
    );
  }