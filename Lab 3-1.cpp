#include<iostream>
using namespace std;
class CircularQueue{
	int size;
	int front;
	int rear;
	int *data;
	public:
		CircularQueue(){
			size=5;
			data=new int[size];
			front=-1;
			rear=-1;
		}
		
		CircularQueue(int s){
			size=s;
			data=new int[size];
		}
		
		bool enqueue(int element){
		if((rear+1)%size==front){      //full
			front=(front+1)%size;
		}
		
		if(front==-1){
			front=0;
		}
		
		rear=(rear+1)%size;
		data[rear]=element;
		return true;
		}
		
		
		int deueue(){
			if(front==-1 && rear==-1){
				cout<<"Empty.\n";
				return -1;
			}
			
			int res=data[front];
			
			if(front==rear){
				rear=-1;
				front=-1;
			}
			
			else
			front=(front+1)%size;
			
			return res;
		}
		
		
		int top(){
			if(front==-1 && rear==-1)
			return -1;
			return data[front];
		}
		
		
		void display(){
			if(front==-1 && rear==-1){
				cout<<"Empty.\n";
			}
			
			else{
				int i=front;
				while(i!=rear){
					cout<<data[i]<<" ";
					i=(i+1)%size;
				}
				cout<<data[rear]<<endl;
				
			}
		}
		
		
			int totalElements() {
        if (front == -1) {
            return 0;  // Queue is empty
        }

        if (front <= rear) {
            return rear - front + 1;  // Normal case
        } else {
            return size - front + rear + 1;  // Circular case
        }
    

		}
		
		
		 ~CircularQueue() {
        delete[] data;
    }
		
};

int main(){
	CircularQueue * q = new CircularQueue (6);
cout << q->enqueue(5) << endl;
cout << q->enqueue(10) << endl;
cout << q->enqueue(15) << endl;
cout << q->enqueue(20) << endl;
cout << q->enqueue(25) << endl;
cout << q->enqueue(25) << endl;

cout<<"Contents are:\n";
q->display();

cout<<"Element deleted is: "<<q->deueue()<<endl;

cout<<"Top element is: "<<q->top()<<endl;

cout<<"Total Elements are: "<<q->totalElements()<<endl;

cout << q->enqueue(40) << endl;
cout << q->enqueue(50) << endl;

cout<<"Total Elements are: "<<q->totalElements()<<endl;
q->display();


return 0;

	
}
