function Navbar() {
  return (
    <nav className="sticky top-0 z-50 bg-slate-900/80 backdrop-blur border-b border-slate-700">
      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        <h1 className="text-3xl font-bold text-white">
          🤖 <span className="text-blue-400">StudyAI</span>
        </h1>

        <div className="hidden md:flex gap-6 text-slate-300">
          <a href="#" className="hover:text-blue-400 transition">
            Summary
          </a>
          <a href="#" className="hover:text-blue-400 transition">
            Flashcards
          </a>
          <a href="#" className="hover:text-blue-400 transition">
            Schedule
          </a>
          <a href="#" className="hover:text-blue-400 transition">
            Quiz
          </a>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
