# VGC-Team-Grab
Used for grabbing Pokemon teams from VGC video feeds.

## Motivation

Pokemon Showdown (play.pokemonshowdown.com) provides a lot of inherent logging capability due to its existence as a browser based battle simulator. However, cartridge based gameplay lacks these capabilities. In addition, the official VGC circuit is completely cartridge based. However, we do have a wealth of video data from previous tournaments and upcoming ones. By using this video data, we can automatically log what teams were used based on the team preview screen, thus making it easier to create usage stats later down the line.

Usage of such a utility is not just limited to the VGC circuit. Those with access to 3DS video recording (capture card or homebrewed New Nintendo 3DS) can also use this to monitor their own video feeds at home. This means that anyone should be able to get an empirical measurement of usage stats.

An example here is shown from Ray Rizzo's Youtube series "Rayce to the Top". Youtube might become a wealth of information with which we can grab Battle Spot data.

https://raw.githubusercontent.com/mattsybeldon/VGC-Team-Grab/3af3887a35baf9992cf0c88fa41882ab440af8e9/readme/tp_example.png

## Usage

You will need:

1. Python 2
2. OpenCV
3. SciKit-Learn
4. pip if ripping your own sprites for whatever reason

Will fill this out once things develop.

## History

1/17 - Initial commit. Made scripts to generate labelled sprites that will be our ground truths.

1/18 - Team preview screen classifier developed. Uses template matching scores and SVM. Seems to work nicely so far.

1/18 - Added classifier and features for detecting Pokemon on Team Preview. Untested since I still have to generate more training data.

1/18 - Got a configuration script running to pick the monitoring region. This combined with the auto resize should make usage easier.

1/19 - Wrote the nearest neighbor classifier for finding what Pokemon we're looking at. At this stage all individual classifiers should have at least an initial draft. Next step is to glue them all together and see performance on real world data.

1/20 - Building up the main function and testing the flow of it. Squashed a bug with path names that I stupidly did. Collected information that we'll need to extract Pokemon from specific spots.

1/21 - Got everything in the main written up except for the logging. The process itself "works" but isn't robust yet. Will be collecting some training data to correct that.

1/25 - Everything is now in place. The last steps are now to get the nearest neighbor classifier for Pokemon ID'ing more robust and to interface with OBS/XSplit for stream automation.

## Credits
trainertower.com - For providing the sprites.
