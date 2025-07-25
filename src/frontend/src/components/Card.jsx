import React from 'react';

export default function Card({
  title,
  children,
  bgColor,
  textColor = '#7B513F',
  progressCount = 0,
}) {
  return (
    <div
      className="w-max p-6 min-w-[330px] rounded-2xl flex flex-col justify-between"
      style={{ backgroundColor: bgColor, color: textColor }}
    >
      <h2 className="text-xl font-semibold mb-4">{title}</h2>

      {/* Main content area (chart, preview, text) */}
      <div className="mb-4">
        {children}
      </div>

      {/* Progress circles (if any) */}
      {progressCount > 0 && (
        <div className="flex space-x-2">
          {Array.from({ length: progressCount }).map((_, i) => (
            <span
              key={i}
              className="w-4 h-4 bg-white rounded-full"
            />
          ))}
        </div>
      )}
    </div>
  );
}
