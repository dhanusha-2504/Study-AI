function Flashcard({ question, answer }) {
  return (
    <div
      className="
      bg-slate-800
      border
      border-slate-700
      rounded-2xl
      p-6
      shadow-lg
      hover:scale-[1.02]
      transition
      "
    >
      <h3 className="text-xl font-bold text-blue-400 mb-4">
        ❓ {question}
      </h3>

      <p className="text-slate-300">
        {answer}
      </p>
    </div>
  );
}

export default Flashcard;