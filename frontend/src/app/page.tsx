"use client";
import { useState } from 'react';
import { Search, Loader2, Atom, Sparkles } from 'lucide-react';
import ReactMarkdown from 'react-markdown';

export default function Home() {
  const [topic, setTopic] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState('');

  const handleResearch = async () => {
    if (!topic) return;
    setLoading(true);
    try {
      // ⚠️ IMPORTANT: Paste your Codespace backend URL here!
      const response = await fetch('https://animated-space-broccoli-v9xw9q9gj772wjj4-8000.app.github.dev/research', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic }),
      });
      const data = await response.json();
      setResult(data.content_draft);
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-[#f8fafc] py-12 px-4">
      <div className="max-w-3xl mx-auto">
        
        {/* LOGO & HEADER */}
        <header className="flex flex-col items-center mb-12">
          <div className="bg-blue-600 p-4 rounded-3xl mb-4 shadow-xl shadow-blue-100 ring-4 ring-white">
            <Atom size={42} className="text-white" />
          </div>
          <h1 className="text-5xl font-black text-gray-900 tracking-tighter">
            AI<span className="text-blue-600">Res</span>
          </h1>
          <p className="text-gray-500 mt-2 font-medium flex items-center gap-2">
            <Sparkles size={16} className="text-blue-400" />
            Autonomous Multi-Agent Research Engine
          </p>
        </header>

        {/* INPUT BOX */}
        <div className="bg-white p-2 rounded-2xl shadow-xl border border-gray-100 flex gap-2 mb-10">
          <input 
            className="flex-1 bg-transparent px-4 py-3 outline-none text-gray-800 font-medium"
            placeholder="What should AIRes research today?"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
          />
          <button 
            onClick={handleResearch}
            disabled={loading}
            className="bg-blue-600 text-white px-8 py-3 rounded-xl font-bold hover:bg-blue-700 transition-colors flex items-center gap-2"
          >
            {loading ? <Loader2 className="animate-spin" size={20} /> : <Search size={20} />}
            {loading ? 'Processing...' : 'Research'}
          </button>
        </div>

        {/* RENDERED RESULT */}
        {result && (
          <div className="bg-white p-10 rounded-3xl shadow-2xl border border-gray-100">
            {/* The "prose" class applies the Tailwind Typography styles automatically */}
            <article className="prose prose-blue prose-lg max-w-none text-gray-800 prose-headings:text-gray-900 prose-strong:text-blue-700">
              <ReactMarkdown>
                {result}
              </ReactMarkdown>
            </article>
          </div>
        )}
      </div>
    </main>
  );
}