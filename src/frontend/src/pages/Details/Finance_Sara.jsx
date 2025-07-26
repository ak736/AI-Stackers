// src/pages/Details/Finance_Sara.jsx
import React from 'react';
import { useLocation } from 'react-router-dom';

export default function Finance_Sara() {
  // grab the prompt object passed via navigate()
  const { state } = useLocation();
  const prompt = state?.prompt || { 
    label: 'Finance Advisor Sara', 
    color: 'rgba(211,230,255,0.5)' 
  };

  return (
    <div className="min-h-screen py-6 px-8" style={{ backgroundColor: '#FFFDF5' }}>
      <h1
        className="text-2xl font-bold mb-4"
        style={{ color: '#7B513F', fontFamily: 'Crimson Text, serif' }}
      >
        {prompt.label}
      </h1>

      {/* Summary card */}
      <div
        className="p-4 rounded-2xl flex items-center justify-between mb-6"
        style={{ backgroundColor: prompt.color, border: '1px solid #7B513F' }}
      >
        <div>
          <p className="text-3xl font-bold" style={{ color: '#7B513F' }}>XX% used</p>
          <p style={{ color: '#7B513F' }}>total number</p>
        </div>
        <div
          className="rounded-full flex items-center justify-center"
          style={{ backgroundColor: '#4169E1', width: 56, height: 56 }}
        >
          piechart
        </div>
      </div>

      {/* Breakdown section (to implement next) */}
      <div>
        <p style={{ color: '#7B513F' }}>
          detail breakdown with % bar for each (adjustable)
        </p>
      </div>
    </div>
  );
}
