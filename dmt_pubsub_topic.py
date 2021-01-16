from dm_helper import GaFlattenerDeploymentConfiguration
def GenerateConfig(ctx):

    config = GaFlattenerDeploymentConfiguration(ctx.env)

    resources = {
      'resources': [{
          'name': 'topic-name',
          'type': 'gcp-types/pubsub-v1:projects.topics',
          'properties': {
              'topic': config.get_topic_name()
          },
      'accessControl':
          {'gcpIamPolicy':
              {'bindings':[{
                 'role': 'roles/pubsub.publisher',
                 'members': ["serviceAccount:cloud-logs@system.gserviceaccount.com"]
              }]}
          }
        }]
      }
    return resources