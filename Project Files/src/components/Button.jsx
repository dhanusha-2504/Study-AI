function Button({ title, onClick, loading }) {
  return (
    <button
      onClick={onClick}
      disabled={loading}
      className="
      px-7
      py-4
      rounded-xl
      bg-gradient-to-r
      from-blue-500
      to-indigo-600
      text-white
      font-semibold
      shadow-lg
      hover:scale-105
      hover:shadow-blue-500/40
      transition-all
      duration-300
      disabled:opacity-60
      disabled:cursor-not-allowed
      "
    >
      {loading ? "🤖 AI is Thinking..." : title}
    </button>
  );
}

export default Button;