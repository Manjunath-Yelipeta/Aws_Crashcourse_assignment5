import torch
import gradio as gr
import torchvision.transforms as T
import boto3
import botocore
import traceback



def demo():
    """Demo function.
    Args:
        cfg (DictConfig): Configuration composed by Hydra.
    Returns:
        Tuple[dict, dict]: Dict with metrics and dict with all instantiated objects.
    """

    # log.info("Running Demo")

    # log.info(f"Instantiating scripted model")
    
    print("Downloading model from S3")
    BUCKET_NAME = "test-bucket5-emlo"
    KEY = "aws_crash_course_assignment5/model.script.pt"
    file = "/opt/src/model.script.pt"
    s3 = boto3.resource('s3')

    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, file)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    print("Model downloaded, and saved to /opt/src/model.script.pt")


    model = torch.jit.load('model.script.pt')
    model.eval()

    # log.info(f"Loaded Model: {model}")

    def recognize_digit(image):
        if image is None:
            return None
        image = T.ToTensor()(image).unsqueeze(0)
        try:
            preds = model.forward_jit(image)
        except Exception:
            traceback.print_exc()
        preds = preds[0].tolist()
        label = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
        return {label[i]: preds[i] for i in range(10)}

    
    im = gr.Image(shape=(32, 32))
    demo = gr.Interface(
        fn=recognize_digit,
        inputs=[im],
        outputs=[gr.Label(num_top_classes=10)],
        live=True,
    )
    demo.launch(server_name="0.0.0.0", server_port=80)


if __name__ == "__main__":
    demo()