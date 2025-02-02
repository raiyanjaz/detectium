"use client";

import { useEffect, useState } from 'react';

export default function HeartbeatTracking() {
  const [heartRate, setHeartRate] = useState('N/A');
  const [avgHeartRate, setAvgHeartRate] = useState('N/A');
  const [isScanning, setIsScanning] = useState(false);

  useEffect(() => {
    // Function to fetch serial data from Flask backend
    const fetchSerialData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/get_serial_data');
        if (!response.ok) {
          throw new Error('Failed to fetch serial data');
        }
        const data = await response.json();
        setHeartRate(data.bpm);
        setAvgHeartRate(data.avg_bpm);
        setIsScanning(data.finger_detected === 1); // Assume '1' means scanning
      } catch (error) {
        console.error('Error fetching serial data:', error);
      }
    };

    // Poll the backend every 2 seconds
    const interval = setInterval(fetchSerialData, 2000);
    return () => clearInterval(interval); // Cleanup interval on unmount
  }, []);

  return (
    <div className="col-md-8 border p-3" style={{ borderColor: '#d3d3d3' }}>
      <h4>Heartbeat Tracking</h4>
      <div className="d-flex flex-column flex-md-row justify-content-between" style={{ backgroundColor: '#f8f9fa', padding: '20px', borderRadius: '5px' }}>

        {/* Heart Rate Section */}
        <div className="text-center border p-3 me-md-3" style={{ flex: 1, borderColor: '#d3d3d3', borderRadius: '5px' }}>
          <h5>Heart Rate</h5>
          <p style={{ fontSize: '1.5rem', fontWeight: 'bold' }}>{heartRate} bpm</p>
        </div>

        {/* Average Heart Rate Section */}
        <div className="text-center border p-3 me-md-3" style={{ flex: 1, borderColor: '#d3d3d3', borderRadius: '5px' }}>
          <h5>Average Heart Rate</h5>
          <p style={{ fontSize: '1.5rem', fontWeight: 'bold' }}>{avgHeartRate} bpm</p>
        </div>

        {/* Scanning Status Section */}
        <div className="text-center border p-3" style={{ flex: 1, borderColor: '#d3d3d3', borderRadius: '5px' }}>
          <h5>Status</h5>
          <p
            style={{
              fontSize: '1.5rem',
              fontWeight: 'bold',
              color: isScanning ? 'green' : 'red',
            }}
          >
            {isScanning ? 'Scanning' : 'Not Scanning'}
          </p>
        </div>

      </div>
    </div>
  );
}
