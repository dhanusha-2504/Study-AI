function getOptionLabel(value = "") {
    const match = String(value).trim().match(/^([a-d])\s*[.):-]?\s*/i);
    return match ? match[1].toLowerCase() : null;
}

function normalizeOptionText(value = "") {
    return String(value)
        .trim()
        .replace(/^([a-d])\s*[.):-]+\s*/i, "")
        .trim()
        .toLowerCase()
        .replace(/\s+/g, "")
        .replace(/[^a-z0-9+/=-]/g, "");
}

export function normalizeQuizOption(value = "") {
    return normalizeOptionText(value);
}

export function isQuizOptionCorrect(selectedOption, correctAnswer) {
    const selectedLabel = getOptionLabel(selectedOption);
    const correctLabel = getOptionLabel(correctAnswer);

    if (selectedLabel && correctLabel && selectedLabel === correctLabel) {
        return true;
    }

    const normalizedSelected = normalizeQuizOption(selectedOption);
    const normalizedCorrect = normalizeQuizOption(correctAnswer);

    return normalizedSelected === normalizedCorrect;
}

export function getCorrectQuizOption(question) {
    if (!question || !Array.isArray(question.options)) {
        return null;
    }

    const answer = question.answer;
    if (!answer) {
        return null;
    }

    return question.options.find((option) => isQuizOptionCorrect(option, answer)) || null;
}
