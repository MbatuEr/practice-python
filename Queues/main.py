from Queues import AnimalShelter

if __name__ == "__main__":
    shelter = AnimalShelter()

    shelter.enqueue("dog")
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("cat")

    try:
        adopted1 = shelter.dequeue_any()
        print(f"Adopted: {adopted1.animal_type} with order: {adopted1.order}")

        adopted2 = shelter.dequeue_dog()
        print(f"Adopted: {adopted2.animal_type} with order: {adopted2.order}")

        adopted3 = shelter.dequeue_cat()
        print(f"Adopted: {adopted3.animal_type} with order: {adopted3.order}")

    except RuntimeError as e:
        print(e)