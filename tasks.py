# -*- coding: utf-8 -*-
from invoke import run, task 
from NeuralNetworkLanguageModel import * 
import DataSet

@task
def clean():
    run("rm *.pyc")

@task
def train(modelPath):
    trainingData = [u"あこんにちは:わたし:の:なまえ:は:にぼじろう:です||こんにちは:わたし:の:なまえ:は:にぼじろう:です||こんにちは:わたし:の:なまえ:は:にぼじろう:です||あなた:が:かの:ゆうめいな:にぼじろう:さん:ですか",
                    u"ちは:わ:の:まえ:は:にろう:です||にちは:たし:の:まえ:は:にう:です||ちは:わたし:の:なまえ:は:うひゃひゃ:うひひ||ほげげ:が:かの:めいな:にぼじろう:さん:でか",
                    u"ちは:わ:の:まえ:は:にろう:です||にちは:たし:の:まえ:は:にう:です||ちは:わたし:の:なまえ:は:うひゃひゃ:うひひ||ほげげ:が:かの:めいな:にぼじろう:さん:で",
                    u"ちは:わ:の:まえ:は:にろう:です||にちは:たし:の:まえ:は:にう:です||ちは:わたし:の:なまえ:は:うひゃひゃ:うひひ||ほげげ:が:かの:めいな:にぼじろう:さん:で"]
    labels = np.array([1,1,1,1])
    lm = NeuralNetworkLanguageModel()
    lm.train(trainingData, labels, savePath = modelPath)

@task
def test(modelPath):
    testData = [u"あこんにちは:わたし:の:なまえ:は:にぼじろう:です||こんにちは:わたし:の:なまえ:は:にぼじろう:です||こんにちは:わたし:の:なまえ:は:にぼじろう:です||あなた:が:かの:ゆうめいな:にぼじろう:さん:ですか",
                    u"ちは:わ:の:まえ:は:にろう:です||にちは:たし:の:まえ:は:にう:です||ちは:わたし:の:なまえ:は:うひゃひゃ:うひひ||ほげげ:が:かの:めいな:にぼじろう:さん:でか",
                    u"ちは:わ:の:まえ:は:にろう:です||にちは:たし:の:まえ:は:にう:です||ちは:わたし:の:なまえ:は:うひゃひゃ:うひひ||ほげげ:が:かの:めいな:にぼじろう:さん:で",
                    u"ちは:わ:の:まえ:は:にろう:です||にちは:たし:の:まえ:は:にう:です||ちは:わたし:の:なまえ:は:うひゃひゃ:うひひ||ほげげ:が:かの:めいな:にぼじろう:さん:で"]
    lm = NeuralNetworkLanguageModel()
    print lm.predict(testData, modelPath)

@task
def createData(inputFilename, outputFilename):
    DataSet.createData(inputFilename, outputFilename)
