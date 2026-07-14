import test from 'node:test';
import assert from 'node:assert/strict';

import { isQuizOptionCorrect } from './quizUtils.js';

test('treats answer matching as case-insensitive and whitespace-tolerant', () => {
    assert.equal(isQuizOptionCorrect('Paris', ' paris '), true);
    assert.equal(isQuizOptionCorrect(' 2 + 2 ', '2+2'), true);
    assert.equal(isQuizOptionCorrect('C. 1999', '1999'), true);
});

test('matches option labels when the answer is a letter and the option text is full text', () => {
    assert.equal(isQuizOptionCorrect('A', 'A. The main idea of the document'), true);
    assert.equal(isQuizOptionCorrect('A. The main idea of the document', 'A'), true);
});
