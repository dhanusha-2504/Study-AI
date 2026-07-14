function Hero() {
  return (
    <section className="py-16 text-center">

      <h1 className="text-6xl font-extrabold text-white leading-tight">
        Study Smarter with
        <span className="text-blue-500"> AI</span>
      </h1>

      <p className="mt-6 text-xl text-slate-400 max-w-3xl mx-auto">
        Upload your study material and instantly generate AI-powered
        summaries, flashcards, quizzes and personalized study schedules.
      </p>

      <div className="mt-10 flex justify-center gap-6 flex-wrap">

        <div className="bg-slate-800 rounded-xl px-6 py-4 shadow-lg">
          📄 AI Summary
        </div>

        <div className="bg-slate-800 rounded-xl px-6 py-4 shadow-lg">
          🃏 Flashcards
        </div>

        <div className="bg-slate-800 rounded-xl px-6 py-4 shadow-lg">
          📅 Study Planner
        </div>

        <div className="bg-slate-800 rounded-xl px-6 py-4 shadow-lg">
          🧠 Quiz Generator
        </div>

      </div>

    </section>
  );
}

export default Hero;