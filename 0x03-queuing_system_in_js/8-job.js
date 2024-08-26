function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');

  const queueName = 'push_notification_code_3';

  jobs.forEach((jobData) => {
    const job = queue.create(queueName, jobData);

    job.save((err) => {
      if (!err) console.log(`Notification job created: ${job.id}`);
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
