import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const prompts = [
  {
    id: 1,
    label: 'plan a emergency wedding in 3 months',
    color: '#D3E6FF',       // blue pill
  },
  {
    id: 2,
    label: 'help me pivot to a new industry in 6 months',
    color: '#E8DDBE',       // yellow pill
  },
  {
    id: 3,
    label: 'train me to lose weight and be marathon ready',
    color: '#D6EFE8',       // green pill
  },
];

export default function Home() {
  const [selectedId, setSelectedId] = useState(null);
  const navigate = useNavigate();

  const handlePlan = () => {
    if (!selectedId) return;
    const chosen = prompts.find(p => p.id === selectedId);
    navigate(`/dashboard/${selectedId}`, { state: { prompt: chosen } });
  };

  return (
    <div
      className="min-h-screen flex items-center justify-center px-4"
      style={{ backgroundColor: '#FFFDF5' }}  // app background
    >
      <div className="w-full max-w-md flex flex-col items-center space-y-6">
        {/* Logo placeholder */}
        <div
          className="rounded-full"
          style={{ backgroundColor: '#A0A0A0', width: 80, height: 80 }}
        />

        {/* App name */}
        <h1 className="text-3xl font-bold" style={{ color: '#4169E1', fontFamily: 'Space Grotesk, sans-serif', fontSize: 30, fontWeight: 300 }}>
          PraxAI
        </h1>

        {/* Subtitle */}
        <p className="text-lg" style={{ color: '#7B513F', fontFamily: 'Crimson Text, serif' }}>
          choose a prompt to see our demo
        </p>

        {/* Prompt pills */}
        <div className="w-full space-y-4">
          {prompts.map(p => (
            <button
              key={p.id}
              onClick={() => setSelectedId(p.id)}
              className={
                `w-full py-3 rounded-full font-medium transform transition-transform duration-150 filter ` +
                (selectedId === p.id
                ? 'brightness-95 scale-105'        // darker + enlarged when selected
                : 'scale-90 hover:brightness-95 hover:scale-105') // slight hover effect
              }
              style={{ 
                backgroundColor: p.color,
                color: '#7B513F'
              }}
            >
              {p.label}
            </button>
          ))}
        </div>

        {/* CTA */}
        <button
          onClick={handlePlan}
          disabled={!selectedId}
          className="mt-20 w-1/2 py-3 rounded-full font-semibold disabled:opacity-50 disabled:cursor-not-allowed"
          style={{
            backgroundColor: '#CE8C70',
            color: '#000000'
          }}
        >
          plan for me!
        </button>
      </div>
    </div>
  );
}
