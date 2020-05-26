count=1
ite=1
def model_nu():
    model.add(Dense(units=512, activation='relu'))
if (count <= 3):
    while (count <= 3):
	if (accuracy < 97.0):
            model=tensorflow.keras.backend.clear_session()
            model = Sequential()
            model.add(Dense(units=512, input_dim=28*28, activation='relu'))
            if (count == 1):
                model_nu()
            if (count == 2):
                model_nu()
                model_nu()
            if (count == 3):
                model_nu()
                model_nu()
                model_nu()
            model.add(Dense(units=10, activation='softmax'))
            model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
            print("iteration no:",ite)
            print("count no:",count)
            fitting = model.fit(X_train, y_train_cat, epochs=epoch,verbose=False)
            accuracy=fitting.history['accuracy'][-1] *100
            print("accuracy is :",accuracy)
            model.summary()
            if (accuracy < 97.0):
                count+=1
                ite+=1
            else:
                model.save("/root/mnist.h5")
	else:
	    break

if(accuracy < 97.0):
    a=("model can't reach the desired accuracy but the accuracy reached after adding ",count,"extra Dense layers is",accuracy,"%")
    f=open("/root/model.txt","w")
    f.write(str(a))
    f.close()
    model.save("/root/mnist.h5")
else:
    a=("we have added the",count,"extra Dense layers to reach the desired accuracy and accuracy is",accuracy,"%")
    f=open("/root/model.txt","w")
    f.write(str(a))
    f.close()
        

f=open("/root/accuracy.txt","w")
f.write(str(accuracy))
f.close()
