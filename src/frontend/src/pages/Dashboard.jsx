// src/pages/Dashboard.jsx
import React from 'react';
import Card from '../components/Card';

export default function Dashboard() {
  // 50%‑opacity backgrounds via rgba()
  const cards = [
    {
      id: 'finance',
      title: 'Finance Advisor Sara',
      bgColor: 'rgba(211,230,255,0.5)', // #D3E6FF @50%
      // flex: text on left, small piechart placeholder on right
      content: (
        <div className="flex items-center justify-between">
          {/* Text holder */}
          <div>
            <p className="text-3xl font-bold">XX% used</p>
            <p className="text-sm">total number</p>
          </div>
          {/* Piechart holder */}
          <div className="bg-[#A7A7A7] w-16 h-16 rounded-full flex items-center justify-center">
            piechart
          </div>
        </div>
      ),
    },
    {
      id: 'designer',
      title: 'Designer Michelle',
      bgColor: 'rgba(232,221,190,0.5)', // #E8DDBE @50%
      content: (
        <>
          <div className="bg-[#A7A7A7] h-24 rounded flex items-center justify-center mb-4">
            moodboard preview
          </div>
        </>
      ),
      progressCount: 4,
    },
    {
      id: 'fitcoach',
      title: 'FitCoach Alex',
      bgColor: 'rgba(200,226,219,0.5)', // #C8E2DB @50%
      // flex: left day info with vertical divider, right class info
      content: (
        <div className="flex items-center">
          <div className="pr-4 border-r border-gray-400">
            <p className="text-3xl font-bold">day 1 / XX</p>
          </div>
          <div className="pl-4">
            <p>class at ?pm tmr</p>
          </div>
        </div>
      ),
    },
    {
      id: 'tutor',
      title: 'Tutor Sam',
      bgColor: 'rgba(226,200,200,0.5)', // #E2C8C8 @50%
      // embedded video placeholder
      content: (
        <div className="bg-[#A7A7A7] h-32 rounded overflow-hidden flex items-center justify-center">
          {/* Replace with <iframe> or <video> when available */}
          Video Placeholder
        </div>
      ),
    },
    {
      id: 'assistant',
      title: 'Assistant Emma',
      bgColor: 'rgba(208,172,124,0.5)', // #D0AC7C @50%
      // flex: left text list, right 4 circles
      content: (
        <div className="flex justify-between items-start">
          <div className="space-y-1">
            <p>guest RSVP invite sent: xx</p>
            <p>attending: xx</p>
            <p>not attending: xx</p>
          </div>
          <div className="flex flex-col space-y-2">
            {Array.from({ length: 4 }).map((_, i) => (
              <span
                key={i}
                className="w-4 h-4 bg-white rounded-full"
              />
            ))}
          </div>
        </div>
      ),
    },
  ];

  return (
  <div className="min-h-screen py-6 px-8 md:px-16" style={{ backgroundColor: '#FFFDF5' }}>
    
    {/* Logo + App Name */}
    <div className="flex items-center space-x-4 mb-6">
      <div
        className="rounded-full"
        style={{ backgroundColor: '#A0A0A0', width: 40, height: 40 }}
      />
      <h1 className="text-xl" style={{ color: '#4169E1', fontFamily: 'Space Grotesk, sans-serif', fontSize: 28, fontWeight: 300}}>
        PraxAI
      </h1>
    </div>

    <h2 className="text-2xl font-bold mb-6" style={{color: '#7B513F', fontFamily: 'Crimson Text, serif'}}>
      counting down to your day!
    </h2>

    <div
      className="grid gap-4"
      style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))' }}
    >
      {cards.map(card => (
        <Card key={card.id} title={card.title} bgColor={card.bgColor} className="w-full max-w-md">
          {card.content}
        </Card>
      ))}
    </div>
  </div>
);

}
