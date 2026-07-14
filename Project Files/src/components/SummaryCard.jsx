function SummaryCard({ summary }) {
  return (
    <div className="mt-10 bg-slate-800 border border-slate-700 rounded-2xl shadow-xl p-8">

      <h2 className="text-3xl font-bold text-white mb-5">
        📄 AI Summary
      </h2>

      <pre
        className="
        whitespace-pre-wrap
        text-slate-300
        leading-8
        font-sans
        "
      >
        {summary}
      </pre>

    </div>
  );
}

export default SummaryCard;