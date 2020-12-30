Nathan Moliterno
12-30-20

Introduction:
	This pair of programs trains a neural network on novel, generated
	images of cells in order to be able to classify new images as being unifected
	vs. parasitized with malaria. The network can then be saved, and accesed
	"remotely" to make new predictions via a client application.

Programs:
 	tfConvoluteMalaria.ipynb
 	deployment_test.py

tfConvoluteMalaria.ipynb:
		After importing the libraries, the program first checks to see if a GPU is
		available for use in training the network, and if that GPU is recognized.\
		It then loads all 12480 images each for the trainging uninfected and
		parasatized classes, as well as 1300 images for each of the testing classes.
	Find average dimensions of images
		the average dimension across all test images is determined. This calculation
		is later used when generating novel images to train from.
	Prepare the data
		An image generator object is created that will generate the novel images used
		during training. The generator is tested for a sample image.
	Create Model
		The convolutional neural network model on which the images are to be trained
		is established. The network consists of three pairs of convolutional and max
		pooling layers, followed by a simple dense layer, and finally a binary output
		layer. Early stopping is also implemented with a patience of two iterations.
	Train Model
		Separate image generators are created for the training and testing groups.
		The network is then trained on the images generated for the training group
		and tested for those generated for the testing group. A maximum number of
		epochs is set to 100, though in my experience, the training phase has never
		reached that maximum before early stopping occurred.
	Evaluate Modal
		Losses, accuracy, precicion, recall, f1-score, and a confusion matrix are all
		reported.
	Sample prediction
		Predition on a new image by the network is tested.
	Save model
		The network is saved into a .h5 file.
	Deployment Practice
		Practice deployment for the network's classification is tested
		within-application (as opposed to between a client and server, as is the
		case for deployment_test.py)

deployment_test.py:
	A link for a simulated client is generated. Upon opening that link in a
	browser, the user can interact with the client application. Here, the user
	can upload any image of a cell. Once submitted, the network will make a
	prediction as to its class, display the uploaded image back to the user,
	output its prediction on the page, and save the uploaded image to an "uploads"
	folder.

Cited Sources:
	The concepts and methods implemented in this project, namely for
	tfConvoluteMalaria.ipynb I learned from Jose Portilla's course "Complete
	Tensorflow 2 and Keras Deep Learning Bootcamp" on Udemy.com.

	The cell images were obtained from the NIH National Library of Medicine at
	https://lhncbc.nlm.nih.gov/publication/pub9932