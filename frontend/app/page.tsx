import 'bootstrap/dist/css/bootstrap.min.css';
import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">Welcome to Next.js + Flask Video Feed</h1>

      <div className="row">
        {/* First Container (Video Feed) */}
        <div className="col-md-6 mb-4">
          <div className="p-4 border border-light rounded" style={{ borderColor: '#d3d3d3', height: '300px' }}>
            <h3>Video Feed</h3>
            <div className={styles.videoContainer} style={{ height: '100%' }}>
              {/* Embed Flask video feed */}
              <img
                src="http://127.0.0.1:5000/video_feed"
                alt="Video Feed"
                style={{ width: '100%', height: '100%', objectFit: 'cover', borderRadius: '5px' }}
              />
            </div>
          </div>
        </div>

        {/* Second Container (Greyed Out) */}
        <div className="col-md-6 mb-4">
          <div className="p-4 border border-light rounded bg-light" style={{ borderColor: '#d3d3d3', height: '300px' }}>
            <h3 className="text-muted">Future Container 1</h3>
          </div>
        </div>

        {/* Third Container (Greyed Out) */}
        <div className="col-md-6 mb-4">
          <div className="p-4 border border-light rounded bg-light" style={{ borderColor: '#d3d3d3', height: '300px' }}>
            <h3 className="text-muted">Future Container 2</h3>
          </div>
        </div>

        {/* Fourth Container (Greyed Out) */}
        <div className="col-md-6 mb-4">
          <div className="p-4 border border-light rounded bg-light" style={{ borderColor: '#d3d3d3', height: '300px' }}>
            <h3 className="text-muted">Future Container 3</h3>
          </div>
        </div>
      </div>
    </div>
  );
}
