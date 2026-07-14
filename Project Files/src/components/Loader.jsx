function Loader() {
  return (
    <div className="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50">
      <div className="bg-slate-800 p-8 rounded-2xl shadow-2xl text-center">

        <div className="w-16 h-16 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto"></div>

        <h2 className="text-white text-2xl mt-6 font-bold">
          AI is working...
        </h2>

        <p className="text-slate-400 mt-2">
          Please wait while we process your study material.
        </p>

      </div>
    </div>
  );
}

export default Loader;