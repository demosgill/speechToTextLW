# speechToTextLW
Package for transforming voice into text format.

To transform you own speech into .txt format, run the following on your terminal within speechToTextLW/.

1) python setup.py install
2) python main.py 5 default.txt

The first part will install the package, while the second excerpt will use your microphone to listen to you for 5 seconds.
The output (default.txt) is a text file containing the transcription of your audio into text readable format.

See more here: https://test.pypi.org/project/SpeechToText-GD/1.0.1/

One can also install the package directly through the Python repository using:
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps SpeechToText_GD
