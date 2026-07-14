function TextInput({ value, onChange }) {
  return (
    <textarea
      rows={12}
      value={value}
      onChange={onChange}
      placeholder="Paste your study material here..."
      className="w-full border border-gray-300 rounded-xl p-4"
    />
  );
}

export default TextInput;